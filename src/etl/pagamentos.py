# Databricks notebook source
# MAGIC %sql
# MAGIC select *
# MAGIC from silver.olist.item_pedido

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC with tb_join as (
# MAGIC select t2.*,
# MAGIC         t3.idVendedor
# MAGIC
# MAGIC from silver.olist.pedido as t1
# MAGIC
# MAGIC LEFT JOIN silver.olist.pagamento_pedido as t2
# MAGIC on t1.idPedido = t2.idPedido
# MAGIC
# MAGIC LEFT JOIN silver.olist.item_pedido as t3
# MAGIC on t1.idPedido = t3.idPedido
# MAGIC
# MAGIC where dtPedido <= '2018-01-01' and dtPedido >= add_months('2018-01-01',-6)
# MAGIC ), tb_group AS (
# MAGIC
# MAGIC select idVendedor,
# MAGIC       descTipoPagamento,
# MAGIC       count(distinct idPedido) as qtdePedidoMeioPagamento,
# MAGIC       sum(vlPagamento) as vlPedidoMeioPagamento
# MAGIC from tb_join
# MAGIC WHERE idVendedor IS NOT null
# MAGIC
# MAGIC GROUP BY idVendedor,descTipoPagamento
# MAGIC ORDER BY idVendedor,descTipoPagamento)
# MAGIC
# MAGIC select idVendedor,
# MAGIC       sum(case when descTipoPagamento = 'voucher' then qtdePedidoMeioPagamento else 0 end) as qtde_voucher_pedido,
# MAGIC       sum(case when descTipoPagamento = 'debit_card' then qtdePedidoMeioPagamento else 0 end) as qtde_debit_pedido,
# MAGIC       sum(case when descTipoPagamento = 'credit_card' then qtdePedidoMeioPagamento else 0 end) as qtde_credit_pedido,
# MAGIC       sum(case when descTipoPagamento = 'boleto' then qtdePedidoMeioPagamento else 0 end) as qtde_boleto_pedido,
# MAGIC
# MAGIC       sum(case when descTipoPagamento = 'voucher' then vlPedidoMeioPagamento else 0 end) as valor_voucher_pedido,
# MAGIC       sum(case when descTipoPagamento = 'debit_card' then vlPedidoMeioPagamento else 0 end) as valor_debit_pedido,
# MAGIC       sum(case when descTipoPagamento = 'credit_card' then vlPedidoMeioPagamento else 0 end) as valor_credit_pedido,
# MAGIC       sum(case when descTipoPagamento = 'boleto' then vlPedidoMeioPagamento else 0 end) as valor_boleto_pedido,
# MAGIC
# MAGIC       sum(case when descTipoPagamento = 'voucher' then qtdePedidoMeioPagamento else 0 end)/sum(qtdePedidoMeioPagamento) as pct_qtd_voucher_pedido,
# MAGIC       sum(case when descTipoPagamento = 'debit_card' then qtdePedidoMeioPagamento else 0 end) /sum(qtdePedidoMeioPagamento) as pct_qtd_debit_pedido,
# MAGIC       sum(case when descTipoPagamento = 'credit_card' then qtdePedidoMeioPagamento else 0 end) /sum(qtdePedidoMeioPagamento) as pct_qtd_credit_pedido,
# MAGIC       sum(case when descTipoPagamento = 'boleto' then qtdePedidoMeioPagamento else 0 end) /sum(qtdePedidoMeioPagamento) as pct_qtd_boleto_pedido,
# MAGIC
# MAGIC       sum(case when descTipoPagamento = 'voucher' then vlPedidoMeioPagamento else 0 end)/sum(vlPedidoMeioPagamento) as pct_valor_voucher_pedido,
# MAGIC       sum(case when descTipoPagamento = 'debit_card' then vlPedidoMeioPagamento else 0 end)/sum(vlPedidoMeioPagamento) as pct_qtd_debit_pedido,
# MAGIC       sum(case when descTipoPagamento = 'credit_card' then vlPedidoMeioPagamento else 0 end)/sum(vlPedidoMeioPagamento) as pct_valor_credit_pedido,
# MAGIC       sum(case when descTipoPagamento = 'boleto' then vlPedidoMeioPagamento else 0 end)/sum(vlPedidoMeioPagamento) as pct_valor_boleto_pedido
# MAGIC
# MAGIC
# MAGIC       
# MAGIC from tb_group
# MAGIC group by 1;
# MAGIC
# MAGIC
# MAGIC
