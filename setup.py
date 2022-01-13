from setuptools import setup
import os
from glob import glob #위에 2개 추가
package_name = 'calculator_srv_parameter_launch'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*_launch.py')),#추가
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lsc',
    maintainer_email='chulslee20@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "custom_service_server_node = calculator_srv_parameter_launch.custom_service_server:main",
            "custom_service_client_node = calculator_srv_parameter_launch.custom_service_client:main",
        ],
    },
)
