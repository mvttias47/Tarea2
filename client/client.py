import sys
import os


sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'order-service'))

import grpc
import order_pb2
import order_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = order_pb2_grpc.OrderServiceStub(channel)
        response = stub.PlaceOrder(order_pb2.OrderRequest(
            product_name="Laptop",
            price=1200.0,
            payment_gateway="Webpay",
            card_brand="VISA",
            bank="Banco Estado",
            shipping_address="Calle Falsa 123",
            region="Santiago",
            email="frodoyt332@gmail.com"
        ))
        print("Pedido realizado: ", response.status)

if __name__ == '__main__':
    run()
