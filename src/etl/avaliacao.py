# Databricks notebook source
# MAGIC %sql
# MAGIC with tb_pedido as (
# MAGIC SELECT DISTINCT  t1.idPedido, t2.idVendedor
# MAGIC
# MAGIC FROM silver.olist.pedido as t1
# MAGIC
# MAGIC LEFT JOIN silver.olist.item_pedido as t2
# MAGIC ON t1.idPedido = t2.idPedido
# MAGIC
# MAGIC WHERE t1.dtPedido < '2018-01-01'
# MAGIC and t1.dtPedido >= add_months('2018-01-01', -6) AND idVendedor is not NULL),
# MAGIC tb_join as (
# MAGIC SELECT  t1.*,t2.vlNota
# MAGIC FROM tb_pedido as t1
# MAGIC LEFT JOIN silver.olist.avaliacao_pedido as t2
# MAGIC ON t1.idPedido = t2.idPedido
# MAGIC
# MAGIC ),
# MAGIC
# MAGIC tb_summary as (
# MAGIC SELECT idVendedor,
# MAGIC         avg(vlNota) as avgNota,
# MAGIC         percentile(vlNota,0.5) as medianNota,
# MAGIC         min(vlNota) as minNota,
# MAGIC         max(vlNota) as maxNota,
# MAGIC         count(vlNota)/ count(idPedido) as pctAvaliacao
# MAGIC
# MAGIC from tb_join
# MAGIC
# MAGIC GROUP BY idVendedor)
# MAGIC
# MAGIC SELECT *
# MAGIC from tb_summary;
