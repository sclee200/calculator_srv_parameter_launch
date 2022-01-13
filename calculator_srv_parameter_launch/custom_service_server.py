import rclpy
import math
from rclpy.node import Node

from arimetic_operator.srv import ArithmeticOperator


class cal():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
    def sub(self):
        return self.a-self.b
    def exp(self):
        return math.exp(self.div())

class CustomServiceServer(Node):

    def __init__(self):
        super().__init__('custom_service_server')
        self.srv = self.create_service(ArithmeticOperator, 'ArithmeticCalculation', self.service_callback)

    def service_callback(self, request, response):
        
        obj=cal(request.num1,request.num2)
        self.get_logger().info('operation %d %s %d' % (request.num1, request.operation_kind, request.num2))
        response.is_success = True
        if request.operation_kind=='+':            
            response.returnval = obj.add()
        elif request.operation_kind=='-':
            response.returnval = obj.sub()
        elif request.operation_kind=='m' or request.operation_kind=='*' :
            response.returnval = obj.mul()
        elif request.operation_kind=='/':
            response.returnval = obj.div()
        elif request.operation_kind=='e':
            response.returnval = obj.exp()
        else:
            response.is_success = False
            self.get_logger().info('operation is not known. try another!')
            
            
        return response


def main(args=None):
    rclpy.init(args=args)

    custom_service_server = CustomServiceServer()

    rclpy.spin(custom_service_server)

    rclpy.shutdown()


if __name__ == '__main__':
    main()