# using resolved_model gpt-4o-2024-08-06# created from response, to create create_db_models.sqlite, with test data
#    that is used to create project
# should run without error in manager 
#    if not, check for decimal, indent, or import issues

import decimal
import logging
import sqlalchemy
from sqlalchemy.sql import func 
from logic_bank.logic_bank import Rule
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, DateTime, Numeric, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from datetime import date   
from datetime import datetime

logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

Base = declarative_base()  # from system/genai/create_db_models_inserts/create_db_models_prefix.py


class Customer(Base):
    """description: Table to store customer details."""
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String)
    phone = Column(String)

    # Derived Attributes
    total_pets = Column(Integer)
    total_spent = Column(Integer)


class Pet(Base):
    """description: Table to store pet details."""
    __tablename__ = 'pet'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    species = Column(String)
    breed = Column(String)
    date_of_birth = Column(Date)
    customer_id = Column(Integer, ForeignKey('customer.id'))


class Product(Base):
    """description: Table to store product details."""
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    price = Column(Integer)
    stock_quantity = Column(Integer)


class Order(Base):
    """description: Table to store order details."""
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_date = Column(DateTime, nullable=False)
    customer_id = Column(Integer, ForeignKey('customer.id'))

    # Derived Attribute
    total_amount = Column(Integer)


class OrderItem(Base):
    """description: Table to store details of order items."""
    __tablename__ = 'order_item'

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('order.id'))
    product_id = Column(Integer, ForeignKey('product.id'))
    quantity = Column(Integer, nullable=False)

    # Derived Attribute
    item_total = Column(Integer)


class Appointment(Base):
    """description: Table to store appointment details for pet services."""
    __tablename__ = 'appointment'

    id = Column(Integer, primary_key=True, autoincrement=True)
    pet_id = Column(Integer, ForeignKey('pet.id'))
    service_type = Column(String)
    date = Column(DateTime)


class Service(Base):
    """description: Table to represent various services offered for pets."""
    __tablename__ = 'service'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    price = Column(Integer)


class PetService(Base):
    """description: Intermediate table to link services provided to pets."""
    __tablename__ = 'pet_service'

    id = Column(Integer, primary_key=True, autoincrement=True)
    pet_id = Column(Integer, ForeignKey('pet.id'))
    service_id = Column(Integer, ForeignKey('service.id'))
    appointment_date = Column(DateTime)


class Supplier(Base):
    """description: Table to store supplier details for products."""
    __tablename__ = 'supplier'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    contact_email = Column(String)


class ProductSupply(Base):
    """description: Intermediate table to link products with suppliers."""
    __tablename__ = 'product_supply'

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('product.id'))
    supplier_id = Column(Integer, ForeignKey('supplier.id'))


class Employee(Base):
    """description: Table to store employee details."""
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    position = Column(String)

    # Derived Attribute
    total_hours_worked = Column(Integer)


class Shift(Base):
    """description: Table to store shift details for employees."""
    __tablename__ = 'shift'

    id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey('employee.id'))
    start_time = Column(DateTime)
    end_time = Column(DateTime)


# ALS/GenAI: Create an SQLite database
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# ALS/GenAI: Prepare for sample data

from datetime import date, datetime

# Test Data for Customer
customer_1 = Customer(id=1, name='John Doe', email='johndoe@example.com', phone='123-456-7890', total_pets=2, total_spent=500)
customer_2 = Customer(id=2, name='Jane Smith', email='janesmith@example.com', phone='987-654-3210', total_pets=1, total_spent=150)
customer_3 = Customer(id=3, name='Tom Brown', email='tombrown@example.com', phone='555-666-7777', total_pets=0, total_spent=0)
customer_4 = Customer(id=4, name='Alice White', email='alicewhite@example.com', phone='222-333-4444', total_pets=3, total_spent=300)

# Test Data for Pet
pet_1 = Pet(id=1, name='Buddy', species='Dog', breed='Labrador', date_of_birth=date(2020, 6, 15), customer_id=1)
pet_2 = Pet(id=2, name='Whiskers', species='Cat', breed='Maine Coon', date_of_birth=date(2019, 8, 12), customer_id=2)
pet_3 = Pet(id=3, name='Goldie', species='Fish', breed='Goldfish', date_of_birth=date(2021, 4, 25), customer_id=1)
pet_4 = Pet(id=4, name='Rex', species='Dog', breed='German Shepherd', date_of_birth=date(2018, 5, 30), customer_id=4)

# Test Data for Product
product_1 = Product(id=1, name='Dog Food', price=20, stock_quantity=100)
product_2 = Product(id=2, name='Cat Toy', price=15, stock_quantity=50)
product_3 = Product(id=3, name='Fish Tank', price=100, stock_quantity=20)
product_4 = Product(id=4, name='Dog Leash', price=10, stock_quantity=150)

# Test Data for Order
order_1 = Order(id=1, order_date=datetime(2023, 5, 20, 10, 30), customer_id=1, total_amount=100)
order_2 = Order(id=2, order_date=datetime(2023, 6, 15, 14, 45), customer_id=1, total_amount=400)
order_3 = Order(id=3, order_date=datetime(2023, 5, 12, 9, 15), customer_id=2, total_amount=150)
order_4 = Order(id=4, order_date=datetime(2023, 6, 22, 11, 10), customer_id=4, total_amount=300)

# Test Data for OrderItem
order_item_1 = OrderItem(id=1, order_id=1, product_id=1, quantity=4, item_total=80)
order_item_2 = OrderItem(id=2, order_id=1, product_id=4, quantity=2, item_total=20)
order_item_3 = OrderItem(id=3, order_id=2, product_id=3, quantity=4, item_total=400)
order_item_4 = OrderItem(id=4, order_id=3, product_id=2, quantity=10, item_total=150)

# Test Data for Appointment
appointment_1 = Appointment(id=1, pet_id=1, service_type='Grooming', date=datetime(2023, 4, 25, 10, 0))
apppointment_2 = Appointment(id=2, pet_id=2, service_type='Checkup', date=datetime(2023, 5, 10, 14, 0))
appointment_3 = Appointment(id=3, pet_id=3, service_type='Grooming', date=datetime(2023, 6, 5, 10, 0))
appointment_4 = Appointment(id=4, pet_id=4, service_type='Vaccination', date=datetime(2023, 5, 15, 15, 30))

# Test Data for Service
service_1 = Service(id=1, name='Grooming', price=50)
service_2 = Service(id=2, name='Checkup', price=30)
service_3 = Service(id=3, name='Vaccination', price=40)
service_4 = Service(id=4, name='Training', price=60)

# Test Data for PetService
pet_service_1 = PetService(id=1, pet_id=1, service_id=1, appointment_date=datetime(2023, 4, 25, 10, 0))
pet_service_2 = PetService(id=2, pet_id=2, service_id=2, appointment_date=datetime(2023, 5, 10, 14, 0))
pet_service_3 = PetService(id=3, pet_id=3, service_id=1, appointment_date=datetime(2023, 6, 5, 10, 0))
pet_service_4 = PetService(id=4, pet_id=4, service_id=3, appointment_date=datetime(2023, 5, 15, 15, 30))

# Test Data for Supplier
supplier_1 = Supplier(id=1, name='Pet Supplies Inc.', contact_email='contact@petsupplies.com')
supplier_2 = Supplier(id=2, name='Animal Goods Co.', contact_email='info@animalgoods.com')
supplier_3 = Supplier(id=3, name='Best Pet Store', contact_email='sales@bestpetstore.com')
supplier_4 = Supplier(id=4, name='Pet World', contact_email='support@petworld.com')

# Test Data for ProductSupply
product_supply_1 = ProductSupply(id=1, product_id=1, supplier_id=1)
product_supply_2 = ProductSupply(id=2, product_id=2, supplier_id=2)
product_supply_3 = ProductSupply(id=3, product_id=3, supplier_id=3)
product_supply_4 = ProductSupply(id=4, product_id=4, supplier_id=4)

# Test Data for Employee
employee_1 = Employee(id=1, name='Peter Manning', position='Manager', total_hours_worked=160)
employee_2 = Employee(id=2, name='Susan Lee', position='Sales Associate', total_hours_worked=140)
employee_3 = Employee(id=3, name='Matt Clark', position='Groomer', total_hours_worked=180)
employee_4 = Employee(id=4, name='Laura Wood', position='Trainer', total_hours_worked=120)

# Test Data for Shift
shift_1 = Shift(id=1, employee_id=1, start_time=datetime(2023, 5, 1, 9, 0), end_time=datetime(2023, 5, 1, 17, 0))
shift_2 = Shift(id=2, employee_id=2, start_time=datetime(2023, 5, 2, 9, 0), end_time=datetime(2023, 5, 2, 17, 0))
shift_3 = Shift(id=3, employee_id=3, start_time=datetime(2023, 5, 3, 10, 0), end_time=datetime(2023, 5, 3, 18, 0))
shift_4 = Shift(id=4, employee_id=4, start_time=datetime(2023, 5, 4, 11, 0), end_time=datetime(2023, 5, 4, 19, 0))



session.add_all([customer_1, customer_2, customer_3, customer_4, pet_1, pet_2, pet_3, pet_4, product_1, product_2, product_3, product_4, order_1, order_2, order_3, order_4, order_item_1, order_item_2, order_item_3, order_item_4, appointment_1, apppointment_2, appointment_3, appointment_4, service_1, service_2, service_3, service_4, pet_service_1, pet_service_2, pet_service_3, pet_service_4, supplier_1, supplier_2, supplier_3, supplier_4, product_supply_1, product_supply_2, product_supply_3, product_supply_4, employee_1, employee_2, employee_3, employee_4, shift_1, shift_2, shift_3, shift_4])
session.commit()
