# Databricks notebook source
# MAGIC %sql
# MAGIC with tb_pedidos as (
# MAGIC   select
# MAGIC     distinct t1.idPedido,
# MAGIC     t2.idVendedor
# MAGIC   from
# MAGIC     silver.olist.pedido as t1
# MAGIC     LEFT JOIN silver.olist.item_pedido as t2 on t1.idPedido = t2.idPedido
# MAGIC   WHERE
# MAGIC     t1.dtPedido <= '2018-01-01'
# MAGIC     AND t1.dtPedido >= add_months('2018-01-01', -6)
# MAGIC     AND t2.idVendedor is not null
# MAGIC ),
# MAGIC tb_join as (
# MAGIC   SELECT
# MAGIC     t1.idVendedor,
# MAGIC     t2.*
# MAGIC   from
# MAGIC     tb_pedidos AS t1
# MAGIC     LEFT JOIN silver.olist.pagamento_pedido as t2 on t1.idPedido = t2.idPedido
# MAGIC ),
# MAGIC tb_group AS (
# MAGIC   select
# MAGIC     idVendedor,
# MAGIC     descTipoPagamento,
# MAGIC     count(distinct idPedido) as qtdePedidoMeioPagamento,
# MAGIC     sum(vlPagamento) as vlPedidoMeioPagamento
# MAGIC   from
# MAGIC     tb_join
# MAGIC   WHERE
# MAGIC     idVendedor IS NOT null
# MAGIC   GROUP BY
# MAGIC     idVendedor,
# MAGIC     descTipoPagamento
# MAGIC   ORDER BY
# MAGIC     idVendedor,
# MAGIC     descTipoPagamento
# MAGIC )
# MAGIC select
# MAGIC   idVendedor,
# MAGIC   sum(
# MAGIC     case
# MAGIC       when descTipoPagamento = 'voucher' then qtdePedidoMeioPagamento
# MAGIC       else 0
# MAGIC     end
# MAGIC   ) as qtde_voucher_pedido,
# MAGIC   sum(
# MAGIC     case
# MAGIC       when descTipoPagamento = 'debit_card' then qtdePedidoMeioPagamento
# MAGIC       else 0
# MAGIC     end
# MAGIC   ) as qtde_debit_pedido,
# MAGIC   sum(
# MAGIC     case
# MAGIC       when descTipoPagamento = 'credit_card' then qtdePedidoMeioPagamento
# MAGIC       else 0
# MAGIC     end
# MAGIC   ) as qtde_credit_pedido,
# MAGIC   sum(
# MAGIC     case
# MAGIC       when descTipoPagamento = 'boleto' then qtdePedidoMeioPagamento
# MAGIC       else 0
# MAGIC     end
# MAGIC   ) as qtde_boleto_pedido,
# MAGIC   sum(
# MAGIC     case
# MAGIC       when descTipoPagamento = 'voucher' then vlPedidoMeioPagamento
# MAGIC       else 0
# MAGIC     end
# MAGIC   ) as valor_voucher_pedido,
# MAGIC   sum(
# MAGIC     case
# MAGIC       when descTipoPagamento = 'debit_card' then vlPedidoMeioPagamento
# MAGIC       else 0
# MAGIC     end
# MAGIC   ) as valor_debit_pedido,
# MAGIC   sum(
# MAGIC     case
# MAGIC       when descTipoPagamento = 'credit_card' then vlPedidoMeioPagamento
# MAGIC       else 0
# MAGIC     end
# MAGIC   ) as valor_credit_pedido,
# MAGIC   sum(
# MAGIC     case
# MAGIC       when descTipoPagamento = 'boleto' then vlPedidoMeioPagamento
# MAGIC       else 0
# MAGIC     end
# MAGIC   ) as valor_boleto_pedido,
# MAGIC   sum(
# MAGIC     case
# MAGIC       when descTipoPagamento = 'voucher' then qtdePedidoMeioPagamento
# MAGIC       else 0
# MAGIC     end
# MAGIC   ) / sum(qtdePedidoMeioPagamento) as pct_qtd_voucher_pedido,
# MAGIC   sum(
# MAGIC     case
# MAGIC       when descTipoPagamento = 'debit_card' then qtdePedidoMeioPagamento
# MAGIC       else 0
# MAGIC     end
# MAGIC   ) / sum(qtdePedidoMeioPagamento) as pct_qtd_debit_pedido,
# MAGIC   sum(
# MAGIC     case
# MAGIC       when descTipoPagamento = 'credit_card' then qtdePedidoMeioPagamento
# MAGIC       else 0
# MAGIC     end
# MAGIC   ) / sum(qtdePedidoMeioPagamento) as pct_qtd_credit_pedido,
# MAGIC   sum(
# MAGIC     case
# MAGIC       when descTipoPagamento = 'boleto' then qtdePedidoMeioPagamento
# MAGIC       else 0
# MAGIC     end
# MAGIC   ) / sum(qtdePedidoMeioPagamento) as pct_qtd_boleto_pedido,
# MAGIC   sum(
# MAGIC     case
# MAGIC       when descTipoPagamento = 'voucher' then vlPedidoMeioPagamento
# MAGIC       else 0
# MAGIC     end
# MAGIC   ) / sum(vlPedidoMeioPagamento) as pct_valor_voucher_pedido,
# MAGIC   sum(
# MAGIC     case
# MAGIC       when descTipoPagamento = 'debit_card' then vlPedidoMeioPagamento
# MAGIC       else 0
# MAGIC     end
# MAGIC   ) / sum(vlPedidoMeioPagamento) as pct_qtd_debit_pedido,
# MAGIC   sum(
# MAGIC     case
# MAGIC       when descTipoPagamento = 'credit_card' then vlPedidoMeioPagamento
# MAGIC       else 0
# MAGIC     end
# MAGIC   ) / sum(vlPedidoMeioPagamento) as pct_valor_credit_pedido,
# MAGIC   sum(
# MAGIC     case
# MAGIC       when descTipoPagamento = 'boleto' then vlPedidoMeioPagamento
# MAGIC       else 0
# MAGIC     end
# MAGIC   ) / sum(vlPedidoMeioPagamento) as pct_valor_boleto_pedido
# MAGIC from
# MAGIC   tb_group
# MAGIC group by
# MAGIC   1;

# COMMAND ----------

# MAGIC %sql
# MAGIC
