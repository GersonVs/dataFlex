#### Tabela `User`:

-   id (primary key) | **integer**
-   username | **varchar/string**
-   first_name | **varchar/string**
-   last_name | **varchar/string**
-   email | **varchar/string**
-   password | **varchar/string**
-   is_active | **boolean**
-   date_joined | **timestamp/ISODate**
-   is_staff | **boolean**
-   last_login | **timestamp/ISODate**
-   phone_number | **varchar/string**
-   is_deleted | **boolean**
-   photo | **varchar/string**

#### Tabela `UserAddress`:

-   id (primary key) | **integer**
-   street | **varchar/string**
-   number | **varchar/string**
-   complement | **varchar/string**
-   district | **varchar/string**
-   city | **varchar/string**
-   state | **varchar/string**
-   zip_code | **varchar/string**
-   user_id (foreign key de `User`) | **integer**

#### Tabela `Product`:

-   id (primary key) | **integer**
-   name | **varchar/string**
-   price | **decimal/double**
-   image | **varchar/string**
-   unity_measure | **varchar/string**

#### Tabela `Order`:

-   id (primary key) | **integer**
-   date | **timestamp/ISODate**
-   total_value | **decimal/double**
-   user_id (foreign key de `User`) | **integer**
-   user_address_id (foreign key de `UserAddress`) | **integer**

#### Tabela `OrderItem`:

-   id (primary key) | **integer**
-   product_id (foreign key de `Product`) | **decimal/double**
-   quantity | **decimal/double**
-   total_value | **decimal/double**
-   order_id (foreign key de `Order`) | **integer**
