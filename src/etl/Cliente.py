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
# MAGIC WHERE dtPedido <= '2018-01-01' and dtPedido >= add_months('2018-01-01', -6))
# MAGIC
# MAGIC select *
# MAGIC from tb_join

# COMMAND ----------


