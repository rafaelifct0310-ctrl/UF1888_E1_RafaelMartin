# Análisis del modelo de datos
#### Como funciona Odoo
1. Tablas -> donde se guarda la información
2. Campos -> datos dentro de las tablas
3. Realaciones -> como se conectan entre sí

Ej. Clientes, Productos, Ventas

#### Entrar en PostgreSQL
```
sudo -u postgres psql
```
![alt text](imagen01.png)

##### Ver base de datos
```
\l
```

![alt text](imagen02.png)

```
\c odoo19
```
![alt text](imagen03.png)

#### Buscar tablas importantes
```
\dt
```
![alt text](imagen04-1.png)

![alt text](imagen05.png)

-------------
| Tipo de dato | Tabla | Observaciones |
| -------------| ------|---------------|
| Clientes    | res_partner | guarda clientes, contactos y empresas |
| Productos  | product_template | guarda información general de los productos |
| Ventas   | sale_order  | guarda los pedidos |
--------------

#### Analizar estructura de tablas
- Toca ver que campos tiene cada tabla y localizar las claves.
```
\d res_partner
\d sale_order
\d product_template
```
