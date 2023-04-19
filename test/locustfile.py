from locust import HttpUser, task, between, TaskSet
from threading import Lock
from decouple import config

class TestViewSet(TaskSet):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'token {config("USER_TOKEN_API")}'
    }

    client_list         = []
    client_address_list = []
    order_list          = []
    product_list        = []
    lock                = Lock()

    # Testes do Consumer

    @task(2)
    def create_client(self):
        payload = {
            "name": "Teste",
            "document": "99999999999",
            "phone_number": "99999999999",
        }
        
        with self.client.post("/consumer/api/clients/", json=payload, headers=self.headers, catch_response=True) as response:
            if response.status_code == 201:
                response.success()

                if len(self.client_list) <= 10:
                    self.client_list.append(response.json()["id"])

            elif response.elapsed.total_seconds() > 15:
                response.failure('Request took too long')
            else:
                response.failure("Received unexpected status code")

    @task(2)
    def create_client_address(self):

        if not len(self.client_list):
            return

        client_id = self.client_list[0]

        payload = {
            "street": "Rua teste",
            "number": "99",
            "district": "Bairro teste",
            "city": "Cidade teste",
            "state": "Estado teste",
            "zip_Code": 99999999,
            "client": client_id
        }
        
        with self.client.post("/consumer/api/client-addresses/", json=payload, headers=self.headers, catch_response=True) as response:
            if response.status_code == 201:
                response.success()

                if len(self.client_address_list) <= 10:
                    self.client_address_list.append(response.json()["id"])

            elif response.elapsed.total_seconds() > 15:
                response.failure('Request took too long')
            else:
                response.failure("Received unexpected status code")
    
    @task(1)
    def update_client(self):

        if not len(self.client_list):
            return

        payload = {
            "name": "Teste",
            "document": "00000000000",
            "phone_number": "99999999999",
        }
        with self.lock:
            client_id = self.client_list[0]
            with self.client.put(f"/consumer/api/clients/{client_id}/", json=payload, headers=self.headers, catch_response=True) as response:
                if response.status_code == 200:
                    response.success()
                elif response.elapsed.total_seconds() > 15:
                    response.failure('Request took too long')
                else:
                    response.failure("Received unexpected status code")

    @task(1)
    def update_client_address(self):

        if not len(self.client_address_list) or not len(self.client_list):
            return

        client_address_id = self.client_address_list[0]
        client_id         = self.client_list[0]

        payload = {
            "street": "Rua teste",
            "number": "99",
            "district": "Bairro teste",
            "city": "Cidade teste",
            "state": "Estado teste",
            "zip_Code": 11111111,
            "client": client_id 
        }
        
        with self.lock:
            with self.client.put(f"/consumer/api/client-addresses/{client_address_id}/", json=payload, headers=self.headers, catch_response=True) as response:
                if response.status_code == 200:
                    response.success()
                elif response.elapsed.total_seconds() > 15:
                    response.failure('Request took too long')
                else:
                    response.failure("Received unexpected status code")

    # @task(1)
    # def delete_client(self):

    #     if not len(self.client_list):
    #         return

    #     client_id = self.client_list[0]
    
    #     with self.client.delete(f"/consumer/api/clients/{client_id}/", headers=self.headers, catch_response=True) as response:
    #         if response.status_code == 204:
    #             response.success()

    #             self.client_id = None
                
    #         elif response.elapsed.total_seconds() > 15:
    #             response.failure('Request took too long')
    #         else:
    #             response.failure("Received unexpected status code")

    # @task(1)
    # def delete_client_address(self):

    #     if self.client_address_id is None:
    #         return
    
    #     with self.client.delete(f"/consumer/api/client-addresses/{self.client_address_id}/", headers=self.headers, catch_response=True) as response:
    #         if response.status_code == 204:
    #             response.success()

    #             self.client_address_id = None
                
    #         elif response.elapsed.total_seconds() > 15:
    #             response.failure('Request took too long')
    #         else:
    #             response.failure("Received unexpected status code")

    @task(3)
    def detail_client(self):
        
        if not len(self.client_list):
            return

        client_id = self.client_list[0]

        with self.client.get(f"/consumer/api/clients/{client_id}/", headers=self.headers, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            elif response.elapsed.total_seconds() > 70:
                response.failure("Request took too long")
            else:
                response.failure("Received unexpected status code")

    @task(3)
    def detail_client_address(self):

        if not len(self.client_address_list):
            return

        client_address_id = self.client_address_list[0]

        with self.client.get(f"/consumer/api/client-addresses/{client_address_id}/", headers=self.headers, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            elif response.elapsed.total_seconds() > 70:
                response.failure("Request took too long")
            else:
                response.failure("Received unexpected status code")

    @task(1)
    def list_clients(self):
        with self.client.get("/consumer/api/clients/", headers=self.headers, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            elif response.elapsed.total_seconds() > 70:
                response.failure("Request took too long")
            else:
                response.failure("Received unexpected status code")

    @task(1)
    def list_client_addresses(self):
        with self.client.get("/consumer/api/client-addresses/", headers=self.headers, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            elif response.elapsed.total_seconds() > 70:
                response.failure("Request took too long")
            else:
                response.failure("Received unexpected status code")


    # Teste do Market

    @task(2)
    def create_product(self):
        payload = {
            "name": "Produto",
            "price": 20.0,
            "unity_measure": "un"
        }
        
        with self.client.post("/market/api/products/", json=payload, headers=self.headers, catch_response=True) as response:
            if response.status_code == 201:
                response.success()

                if len(self.product_list) <= 10:

                    self.product_list.append(response.json()['id'])

            elif response.elapsed.total_seconds() > 15:
                response.failure('Request took too long')
            else:
                response.failure("Received unexpected status code")

    @task(1)
    def update_product(self):
        
        if not len(self.product_list):
            return

        product_id = self.product_list[0]

        payload = {
            "name": "Produto",
            "price": 30.0,
            "unity_measure": "un"
        }
        
        with self.client.put(f"/market/api/products/{product_id}/", json=payload, headers=self.headers, catch_response=True) as response:
            if response.status_code == 200:
                response.success()

            elif response.elapsed.total_seconds() > 15:
                response.failure('Request took too long')
            else:
                response.failure("Received unexpected status code")

    @task(3)
    def detail_product(self):

        if not len(self.product_list):
            return

        product_id = self.product_list[0]


        with self.client.get(f"/market/api/products/{product_id}/", headers=self.headers, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            elif response.elapsed.total_seconds() > 70:
                response.failure("Request took too long")
            else:
                response.failure("Received unexpected status code")

    # @task(1)
    # def delete_product(self):

    #     if not len(self.product_list):
    #         return
    
    #     product_id = self.product_list[0]

    #     with self.client.delete(f"/market/api/products/{product_id}/", headers=self.headers, catch_response=True) as response:

    #         if response.status_code == 204 or response.status_code == 404: # Produto já deletado por outra task (problema de concorrência) 
    #             response.success()
    #             print("STATUS: ", response.status_code)

    #             try:
    #                 self.product_list.pop(self.product_list.index(product_id))
    #             except:
    #                 pass

    #         elif response.elapsed.total_seconds() > 15:
    #             response.failure('Request took too long')
            
    #         else:
    #             response.failure("Received unexpected status code")

    @task(1)
    def list_products(self):
        with self.client.get("/market/api/products/", headers=self.headers, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            elif response.elapsed.total_seconds() > 70:
                response.failure("Request took too long")
            else:
                response.failure("Received unexpected status code")

    
    @task(3)
    def create_order(self):

        if not len(self.client_address_list) or not len(self.client_list):
            return

        client_address_id = self.client_address_list[0]
        client_id         = self.client_list[0]

        if not len(self.product_list):
            return

        payload = {
            "client": client_id,
            "client_address": client_address_id,
            "items": [{'product': product, 'quantity': 5} for product in self.product_list]
        }

        with self.client.post("/market/api/create_order/", json=payload, headers=self.headers, catch_response=True) as response:
            if response.status_code == 201:
                response.success()

                if len(self.order_list) <= 10:
                    self.order_list.append(response.json()['order_id'])

            elif response.elapsed.total_seconds() > 15:
                response.failure('Request took too long')
            else:
                response.failure("Received unexpected status code")
            

    @task(1)
    def detail_order(self):

        if not len(self.order_list):
            return

        with self.lock:
            order_id = self.order_list[0]
            with self.client.get(f"/market/api/detail_order/{order_id}/", headers=self.headers, catch_response=True) as response:
                if response.status_code == 200:
                    response.success()
                elif response.elapsed.total_seconds() > 70:
                    response.failure("Request took too long")
                else:
                    response.failure("Received unexpected status code")

    @task(1)
    def delete_order(self):

        if not len(self.order_list):
            return
        
        with self.lock:
            order_id = self.order_list[0]
            with self.client.delete(f"/market/api/delete_order/{order_id}/", headers=self.headers, catch_response=True) as response:
                
                if response.status_code == 404:
                    response.success()

                    self.order_list.pop(0)
                    self.delete_order()
                
                elif response.status_code == 204:
                    response.success()

                    self.order_list.pop(self.order_list.index(order_id))    

                elif response.elapsed.total_seconds() > 15:
                    response.failure('Request took too long')
                
                elif response.status_code >= 400:
                    response.failure("Received unexpected status code")


class RunLoadTest(HttpUser):
    wait_time = between(3, 5) # Faz com que os usuários simulados esperem entre 3 e 5 segundos após a execução de cada tarefa.
    tasks = [TestViewSet]
