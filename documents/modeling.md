#### Tabela `Client`:

-   id (primary key) | **integer**
-   name | **varchar/string**
-   document | **varchar/string**
-   phone_number | **varchar/string**
-   register_date | **varchar/string**
-   is_active | **varchar/string**
-   is_deleted | **varchar/string**

#### Tabela `ClientAddress`:

-   id (primary key) | **integer**
-   street | **varchar/string**
-   number | **varchar/string**
-   complement | **varchar/string**
-   district | **varchar/string**
-   city | **varchar/string**
-   state | **varchar/string**
-   zip_code | **varchar/string**
-   client_id (foreign key de `Client`) | **integer**

#### Tabela `Product`:

-   id (primary key) | **integer**
-   name | **varchar/string**
-   price | **decimal/double**
-   unity_measure | **varchar/string**

#### Tabela `Order`:

-   id (primary key) | **integer**
-   date | **timestamp/ISODate**
-   total_value | **decimal/double**
-   client_id (foreign key de `Client`) | **integer**
-   user_address_id (foreign key de `UserAddress`) | **integer**

#### Tabela `OrderItem`:

-   id (primary key) | **integer**
-   product_id (foreign key de `Product`) | **decimal/double**
-   quantity | **decimal/double**
-   total_value | **decimal/double**
-   order_id (foreign key de `Order`) | **integer**
