# Databricks notebook source
# MAGIC %sql
# MAGIC WITH tb_pedido as (
# MAGIC SELECT t1.idPedido,
# MAGIC        t2.idVendedor,
# MAGIC        t1.descSituacao,
# MAGIC        t1.dtPedido,
# MAGIC        t1.dtAprovado,
# MAGIC        t1.dtEntregue,
# MAGIC        t1.dtEstimativaEntrega,
# MAGIC        sum(vlFrete) as totalFrete
# MAGIC FROM silver.olist.pedido as t1
# MAGIC
# MAGIC LEFT JOIN silver.olist.item_pedido as t2
# MAGIC ON t1.idPedido = t2.idPedido
# MAGIC
# MAGIC WHERE dtPedido < '2018-01-01' AND dtPedido >= add_months('2018-01-01',-6)
# MAGIC
# MAGIC GROUP BY t1.idPedido,
# MAGIC          t2.idVendedor,
# MAGIC          t1.descSituacao,
# MAGIC          t1.dtPedido,
# MAGIC          t1.dtAprovado,
# MAGIC          t1.dtEntregue,
# MAGIC          t1.dtEstimativaEntrega
# MAGIC )
# MAGIC
# MAGIC select  idVendedor,
# MAGIC         COUNT(DISTINCT CASE WHEN descSituacao = 'delivered' and DATE(COALESCE(dtEntregue,'2018-01-01')) > DATE(dtEstimativaEntrega) THEN idPedido END)/ COUNT(DISTINCT CASE WHEN descSituacao = 'delivered' THEN idPedido END) as pct_PedidoAtraso,
# MAGIC         count(distinct case when descSituacao = 'canceled' then idPedido end)/ 
# MAGIC count(distinct idPedido) as pctPedidoCancelado,
# MAGIC         avg(totalFrete) as avgFrete,
# MAGIC         percentile(totalFrete, 0,5) as mediaFrete,
# MAGIC         max(totalFrete) as maxFrete,
# MAGIC         min(totalFrete) as minFrete,
# MAGIC         avg(datediff(COALESCE(dtEntregue,'2018-01-01'),dtAprovado)) as qtdDiasAprovadoEntrega,
# MAGIC         avg(datediff(COALESCE(dtEntregue,'2018-01-01'),dtPedido)) as qtdDiasPedidoEntrega,
# MAGIC         avg(datediff(dtEstimativaEntrega,COALESCE(dtEntregue,'2018-01-01'))) as qtdDiaEntregaPromessa
# MAGIC         
# MAGIC         
# MAGIC from tb_pedido
# MAGIC
# MAGIC
# MAGIC GROUP BY 1
