# Databricks notebook source
# MAGIC %sql 
# MAGIC WITH tb_pedidos AS (
# MAGIC   SELECT 
# MAGIC     DISTINCT t1.idPedido, 
# MAGIC     t2.idVendedor 
# MAGIC   FROM 
# MAGIC     silver.olist.pedido as t1 
# MAGIC     LEFT JOIN silver.olist.item_pedido as t2 on t1.idPedido = t2.idPedido 
# MAGIC   WHERE 
# MAGIC     t1.dtPedido <= '2018-01-01' 
# MAGIC     AND t1.dtPedido >= add_months('2018-01-01', -6) 
# MAGIC     AND t2.idVendedor is not null
# MAGIC ), 
# MAGIC tb_join AS (
# MAGIC   SELECT 
# MAGIC     t1.idVendedor, 
# MAGIC     t2.* 
# MAGIC   FROM 
# MAGIC     tb_pedidos AS t1 
# MAGIC     LEFT JOIN silver.olist.pagamento_pedido as t2 on t1.idPedido = t2.idPedido
# MAGIC ), 
# MAGIC tb_group AS (
# MAGIC   SELECT 
# MAGIC     idVendedor, 
# MAGIC     descTipoPagamento, 
# MAGIC     count(DISTINCT idPedido) as qtdePedidoMeioPagamento, 
# MAGIC     sum(vlPagamento) as vlPedidoMeioPagamento 
# MAGIC   FROM 
# MAGIC     tb_join 
# MAGIC   WHERE 
# MAGIC     idVendedor IS NOT null 
# MAGIC   GROUP BY 
# MAGIC     idVendedor, 
# MAGIC     descTipoPagamento 
# MAGIC   ORDER BY 
# MAGIC     idVendedor, 
# MAGIC     descTipoPagamento
# MAGIC ), 
# MAGIC tb_summary AS (
# MAGIC   SELECT 
# MAGIC     idVendedor, 
# MAGIC     sum(
# MAGIC       CASE WHEN descTipoPagamento = 'voucher' THEN qtdePedidoMeioPagamento ELSE 0 END
# MAGIC     ) AS qtde_voucher_pedido, 
# MAGIC     sum(
# MAGIC       CASE WHEN descTipoPagamento = 'debit_card' THEN qtdePedidoMeioPagamento ELSE 0 END
# MAGIC     ) AS qtde_debit_pedido, 
# MAGIC     sum(
# MAGIC       CASE WHEN descTipoPagamento = 'credit_card' THEN qtdePedidoMeioPagamento ELSE 0 END
# MAGIC     ) AS qtde_credit_pedido, 
# MAGIC     sum(
# MAGIC       CASE WHEN descTipoPagamento = 'boleto' THEN qtdePedidoMeioPagamento ELSE 0 END
# MAGIC     ) AS qtde_boleto_pedido, 
# MAGIC     sum(
# MAGIC       CASE WHEN descTipoPagamento = 'voucher' THEN vlPedidoMeioPagamento ELSE 0 END
# MAGIC     ) AS valor_voucher_pedido, 
# MAGIC     sum(
# MAGIC       CASE WHEN descTipoPagamento = 'debit_card' THEN vlPedidoMeioPagamento ELSE 0 END
# MAGIC     ) AS valor_debit_pedido, 
# MAGIC     sum(
# MAGIC       CASE WHEN descTipoPagamento = 'credit_card' THEN vlPedidoMeioPagamento ELSE 0 END
# MAGIC     ) AS valor_credit_pedido, 
# MAGIC     sum(
# MAGIC       CASE WHEN descTipoPagamento = 'boleto' THEN vlPedidoMeioPagamento ELSE 0 END
# MAGIC     ) AS valor_boleto_pedido, 
# MAGIC     sum(
# MAGIC       CASE WHEN descTipoPagamento = 'voucher' THEN qtdePedidoMeioPagamento ELSE 0 END
# MAGIC     ) / sum(qtdePedidoMeioPagamento) AS pct_qtd_voucher_pedido, 
# MAGIC     sum(
# MAGIC       case when descTipoPagamento = 'debit_card' then qtdePedidoMeioPagamento else 0 end
# MAGIC     ) / sum(qtdePedidoMeioPagamento) as pct_qtd_debit_pedido, 
# MAGIC     sum(
# MAGIC       case when descTipoPagamento = 'credit_card' then qtdePedidoMeioPagamento else 0 end
# MAGIC     ) / sum(qtdePedidoMeioPagamento) as pct_qtd_credit_pedido, 
# MAGIC     sum(
# MAGIC       case when descTipoPagamento = 'boleto' then qtdePedidoMeioPagamento else 0 end
# MAGIC     ) / sum(qtdePedidoMeioPagamento) as pct_qtd_boleto_pedido, 
# MAGIC     sum(
# MAGIC       case when descTipoPagamento = 'voucher' then vlPedidoMeioPagamento else 0 end
# MAGIC     ) / sum(vlPedidoMeioPagamento) as pct_valor_voucher_pedido, 
# MAGIC     sum(
# MAGIC       case when descTipoPagamento = 'debit_card' then vlPedidoMeioPagamento else 0 end
# MAGIC     ) / sum(vlPedidoMeioPagamento) as pct_qtd_debit_pedido, 
# MAGIC     sum(
# MAGIC       case when descTipoPagamento = 'credit_card' then vlPedidoMeioPagamento else 0 end
# MAGIC     ) / sum(vlPedidoMeioPagamento) as pct_valor_credit_pedido, 
# MAGIC     sum(
# MAGIC       case when descTipoPagamento = 'boleto' then vlPedidoMeioPagamento else 0 end
# MAGIC     ) / sum(vlPedidoMeioPagamento) as pct_valor_boleto_pedido 
# MAGIC   from 
# MAGIC     tb_group 
# MAGIC   group by 
# MAGIC     idVendedor
# MAGIC ),
# MAGIC tb_cartao as (
# MAGIC select idVendedor,
# MAGIC        avg(nrParcelas) as avgQtdeParcelas,
# MAGIC        percentile(nrParcelas, 0.5) as medianQtdeParcelas,
# MAGIC        max(nrParcelas) as maxQtdeParcelas,
# MAGIC        min(nrParcelas) as minQtdeParcelas
# MAGIC from tb_join
# MAGIC where descTipoPagamento = 'credit_card'
# MAGIC group by idvendedor)
# MAGIC
# MAGIC SELECT '2018-01-01' as dtReference,
# MAGIC        t1.*,
# MAGIC        t2.avgQtdeParcelas,
# MAGIC        t2.medianQtdeParcelas,
# MAGIC        t2.maxQtdeParcelas,
# MAGIC        t2.minQtdeParcelas
# MAGIC
# MAGIC from tb_summary as t1
# MAGIC LEFT JOIN tb_cartao as t2
# MAGIC ON t1.idVendedor = t2.idVendedor
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC select *
# MAGIC from olist.silver.
# MAGIC
