from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='calculator_srv_parameter_launch',
            executable='custom_service_server_node', #setup.py's entrypoint와 동일해야함.
            name='custom_service_server_node',
            output='screen',
            emulate_tty=True,
            # parameters=[
            #     {'my_parameter': 'earth'}
            # ]
        ),
        Node(
            package='calculator_srv_parameter_launch',
            executable='custom_service_client_node',
            name='custom_service_client_node',
            output='screen',
            emulate_tty=True,
            # parameters=[
            #     {'my_parameter': 'earth'}
            # ]
        )
    ])