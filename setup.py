from setuptools import find_packages, setup

package_name = 'dp_lab'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/ps5_teleop.launch.py']),
        ('share/' + package_name + '/launch', ['launch/ps5_teleop_basin.launch.py']),
        ('share/' + package_name + '/launch', ['launch/dp_system.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kris',
    maintainer_email='kris@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'ta_node = dp_lab.ta_node:main',
            'ps5_node = dp_lab.ps5_node:main',
            'npo_node = dp_lab.npo_node:main',
            'ps5_node_basin = dp_lab.ps5_node_basin:main',
            'input_node = dp_lab.input_node:main',
            'pathplanner_node = dp_lab.pathplanner_node:main',
            'controller_node = dp_lab.controller_node:main'
        ],
    },
)
