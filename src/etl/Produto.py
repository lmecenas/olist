# Databricks notebook source
# MAGIC %sql
# MAGIC with tb_join as (
# MAGIC SELECT DISTINCT
# MAGIC        t2.idVendedor,
# MAGIC        t3.*
# MAGIC        
# MAGIC
# MAGIC from silver.olist.pedido as t1
# MAGIC
# MAGIC
# MAGIC LEFT JOIN silver.olist.item_pedido as t2
# MAGIC ON t1.idPedido = t2.idPedido
# MAGIC
# MAGIC
# MAGIC LEFT JOIN silver.olist.produto as t3
# MAGIC ON t2.idProduto = t3.idProduto
# MAGIC
# MAGIC WHERE t1.dtPedido < '2018-01-01' 
# MAGIC AND t1.dtPedido >= add_months('2018-01-01', -6)
# MAGIC AND t2.idVendedor IS NOT NULL),
# MAGIC tb_summary as (
# MAGIC
# MAGIC SELECT idVendedor,
# MAGIC         avg(COALESCE(nrFotos,0)) AS avgFotos,
# MAGIC         avg(vlcomprimentocm * vlAlturacm * vlLarguracm) as avgVolumeProduto,
# MAGIC         percentile(vlcomprimentocm * vlAlturacm * vlLarguracm, 0.5) as medianVolumeProduto,
# MAGIC         min(vlcomprimentocm * vlAlturacm * vlLarguracm) as minVolumeProduto,
# MAGIC         max(vlcomprimentocm * vlAlturacm * vlLarguracm) as maxVolumeProduto,
# MAGIC         
# MAGIC         
# MAGIC  
# MAGIC         COUNT( DISTINCT CASE WHEN descCategoria = 'cama_mesa_banho' then idProduto end)/ count(distinct idProduto) as pctCategoriacama_mesa_banho,
# MAGIC         COUNT( DISTINCT CASE WHEN descCategoria = 'beleza_saude' then idProduto end)/ count(distinct idProduto) as pctCategoriabeleza_saude,
# MAGIC         COUNT( DISTINCT CASE WHEN descCategoria = 'esporte_lazer' then idProduto end)/ count(distinct idProduto) as pctCategoriaesporte_lazer,
# MAGIC         COUNT( DISTINCT CASE WHEN descCategoria = 'informatica_acessorios' then idProduto end)/ count(distinct idProduto) as pctCategoriainformatica_acessorios,
# MAGIC         COUNT( DISTINCT CASE WHEN descCategoria = 'moveis_decoracao' then idProduto end)/ count(distinct idProduto) as pctCategoriamoveis_decoracao,
# MAGIC         COUNT( DISTINCT CASE WHEN descCategoria = 'utilidades_domesticas' then idProduto end)/ count(distinct idProduto) as pctCategoriautilidades_domesticas,
# MAGIC         COUNT( DISTINCT CASE WHEN descCategoria = 'relogios_presentes' then idProduto end)/ count(distinct idProduto) as pctCategoriarelogios_presentes,
# MAGIC         COUNT( DISTINCT CASE WHEN descCategoria = 'telefonia' then idProduto end)/ count(distinct idProduto) as pctCategoriatelefonia,
# MAGIC         COUNT( DISTINCT CASE WHEN descCategoria = 'automotivo' then idProduto end)/ count(distinct idProduto) as pctCategoriaautomotivo,
# MAGIC         COUNT( DISTINCT CASE WHEN descCategoria = 'brinquedos' then idProduto end)/ count(distinct idProduto) as pctCategoriabrinquedos,
# MAGIC         COUNT( DISTINCT CASE WHEN descCategoria = 'cool_stuff' then idProduto end)/ count(distinct idProduto) as pctCategoriacool_stuff,
# MAGIC         COUNT( DISTINCT CASE WHEN descCategoria = 'ferramentas_jardim' then idProduto end)/ count(distinct idProduto) as pctCategoriaferramentas_jardim,
# MAGIC         COUNT( DISTINCT CASE WHEN descCategoria = 'perfumaria' then idProduto end)/ count(distinct idProduto) as pctCategoriaperfumaria,
# MAGIC         COUNT( DISTINCT CASE WHEN descCategoria = 'bebes' then idProduto end)/ count(distinct idProduto) as pctCategoriabebes,
# MAGIC         COUNT( DISTINCT CASE WHEN descCategoria = 'eletronicos' then idProduto end)/ count(distinct idProduto) as pctCategoriaeletronicos
# MAGIC         
# MAGIC         
# MAGIC        
# MAGIC from tb_join
# MAGIC group by idVendedor)
# MAGIC
# MAGIC select '2018-01-01' as dtReference, *
# MAGIC from tb_summary

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC        descCategoria
# MAGIC        
# MAGIC        
# MAGIC        
# MAGIC
# MAGIC
# MAGIC FROM silver.olist.item_pedido as t2
# MAGIC
# MAGIC LEFT JOIN silver.olist.produto as t3
# MAGIC ON t2.idProduto = t3.idProduto
# MAGIC
# MAGIC WHERE t2.idVendedor IS NOT NULL
# MAGIC
# MAGIC GROUP BY 1
# MAGIC ORDER BY COUNT(DISTINCT idPedido) DESC
# MAGIC limit 15
