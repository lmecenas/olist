# Databricks notebook source
# MAGIC %sql
# MAGIC with tb_join as (
# MAGIC SELECT DISTINCT 
# MAGIC        t1.idPedido,
# MAGIC        t1.idCliente,
# MAGIC        t2.idVendedor,
# MAGIC        t3.descUF
# MAGIC
# MAGIC
# MAGIC FROM silver.olist.pedido AS t1
# MAGIC LEFT JOIN silver.olist.item_pedido as t2
# MAGIC on t1.idPedido = t2.idPedido
# MAGIC
# MAGIC LEFT JOIN silver.olist.cliente as t3
# MAGIC on t1.idCliente = t3.idCLiente
# MAGIC WHERE dtPedido <= '2018-01-01' AND dtPedido >= add_months('2018-01-01', -6) AND idvendedor is not null),
# MAGIC
# MAGIC tb_group as (
# MAGIC SELECT 
# MAGIC
# MAGIC idVendedor,
# MAGIC count(distinct case when descUF = 'AC' then idPedido end)/ count(distinct idPedido) as pctPedidoAC,
# MAGIC count(distinct case when descUF = 'AL' then idPedido end)/ count(distinct idPedido) as pctPedidoAL,
# MAGIC count(distinct case when descUF = 'AM' then idPedido end)/ count(distinct idPedido) as pctPedidoAM,
# MAGIC count(distinct case when descUF = 'AP' then idPedido end)/ count(distinct idPedido) as pctPedidoAP,
# MAGIC count(distinct case when descUF = 'BA' then idPedido end)/ count(distinct idPedido) as pctPedidoBA,
# MAGIC count(distinct case when descUF = 'CE' then idPedido end)/ count(distinct idPedido) as pctPedidoCE,
# MAGIC count(distinct case when descUF = 'DF' then idPedido end)/ count(distinct idPedido) as pctPedidoDF,
# MAGIC count(distinct case when descUF = 'ES' then idPedido end)/ count(distinct idPedido) as pctPedidoES,
# MAGIC count(distinct case when descUF = 'GO' then idPedido end)/ count(distinct idPedido) as pctPedidoGO,
# MAGIC count(distinct case when descUF = 'MA' then idPedido end)/ count(distinct idPedido) as pctPedidoMA,
# MAGIC count(distinct case when descUF = 'MG' then idPedido end)/ count(distinct idPedido) as pctPedidoMG,
# MAGIC count(distinct case when descUF = 'MS' then idPedido end)/ count(distinct idPedido) as pctPedidoMS,
# MAGIC count(distinct case when descUF = 'MT' then idPedido end)/ count(distinct idPedido) as pctPedidoMT,
# MAGIC count(distinct case when descUF = 'PA' then idPedido end)/ count(distinct idPedido) as pctPedidoPA,
# MAGIC count(distinct case when descUF = 'PB' then idPedido end)/ count(distinct idPedido) as pctPedidoPB,
# MAGIC count(distinct case when descUF = 'PE' then idPedido end)/ count(distinct idPedido) as pctPedidoPE,
# MAGIC count(distinct case when descUF = 'PI' then idPedido end)/ count(distinct idPedido) as pctPedidoPI,
# MAGIC count(distinct case when descUF = 'PR' then idPedido end)/ count(distinct idPedido) as pctPedidoPR,
# MAGIC count(distinct case when descUF = 'RJ' then idPedido end)/ count(distinct idPedido) as pctPedidoRJ,
# MAGIC count(distinct case when descUF = 'RN' then idPedido end)/ count(distinct idPedido) as pctPedidoRN,
# MAGIC count(distinct case when descUF = 'RO' then idPedido end)/ count(distinct idPedido) as pctPedidoRO,
# MAGIC count(distinct case when descUF = 'RR' then idPedido end)/ count(distinct idPedido) as pctPedidoRR,
# MAGIC count(distinct case when descUF = 'RS' then idPedido end)/ count(distinct idPedido) as pctPedidoRS,
# MAGIC count(distinct case when descUF = 'SC' then idPedido end)/ count(distinct idPedido) as pctPedidoSC,
# MAGIC count(distinct case when descUF = 'SE' then idPedido end)/ count(distinct idPedido) as pctPedidoSE,
# MAGIC count(distinct case when descUF = 'SP' then idPedido end)/ count(distinct idPedido) as pctPedidoSP,
# MAGIC count(distinct case when descUF = 'TO' then idPedido end)/ count(distinct idPedido) as pctPedidoTO
# MAGIC
# MAGIC FROM tb_join
# MAGIC GROUP BY idVendedor )
# MAGIC
# MAGIC SELECT '2018-01-01' as dtReference, *
# MAGIC from tb_group

# COMMAND ----------

1) dsadsasdasdasad sdadsadsa dasdasdsa
2
3
4
5
6
7

