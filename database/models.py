# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  November 12, 2024 20:51:30
# Database: sqlite:////tmp/tmp.WpX68eBdvn-01JCH28RYB65NC8JN4H0EFPXZ5/PetShopDataModel/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class Customer(SAFRSBaseX, Base):
    """
    description: Table to store customer details.
    """
    __tablename__ = 'customer'
    _s_collection_name = 'Customer'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String)
    phone = Column(String)
    total_pets = Column(Integer)
    total_spent = Column(Integer)

    # parent relationships (access parent)

    # child relationships (access children)
    OrderList : Mapped[List["Order"]] = relationship(back_populates="customer")
    PetList : Mapped[List["Pet"]] = relationship(back_populates="customer")



class Employee(SAFRSBaseX, Base):
    """
    description: Table to store employee details.
    """
    __tablename__ = 'employee'
    _s_collection_name = 'Employee'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    position = Column(String)
    total_hours_worked = Column(Integer)

    # parent relationships (access parent)

    # child relationships (access children)
    ShiftList : Mapped[List["Shift"]] = relationship(back_populates="employee")



class Product(SAFRSBaseX, Base):
    """
    description: Table to store product details.
    """
    __tablename__ = 'product'
    _s_collection_name = 'Product'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Integer)
    stock_quantity = Column(Integer)

    # parent relationships (access parent)

    # child relationships (access children)
    ProductSupplyList : Mapped[List["ProductSupply"]] = relationship(back_populates="product")
    OrderItemList : Mapped[List["OrderItem"]] = relationship(back_populates="product")



class Service(SAFRSBaseX, Base):
    """
    description: Table to represent various services offered for pets.
    """
    __tablename__ = 'service'
    _s_collection_name = 'Service'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Integer)

    # parent relationships (access parent)

    # child relationships (access children)
    PetServiceList : Mapped[List["PetService"]] = relationship(back_populates="service")



class Supplier(SAFRSBaseX, Base):
    """
    description: Table to store supplier details for products.
    """
    __tablename__ = 'supplier'
    _s_collection_name = 'Supplier'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    contact_email = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    ProductSupplyList : Mapped[List["ProductSupply"]] = relationship(back_populates="supplier")



class Order(SAFRSBaseX, Base):
    """
    description: Table to store order details.
    """
    __tablename__ = 'order'
    _s_collection_name = 'Order'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    order_date = Column(DateTime, nullable=False)
    customer_id = Column(ForeignKey('customer.id'))
    total_amount = Column(Integer)

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("OrderList"))

    # child relationships (access children)
    OrderItemList : Mapped[List["OrderItem"]] = relationship(back_populates="order")



class Pet(SAFRSBaseX, Base):
    """
    description: Table to store pet details.
    """
    __tablename__ = 'pet'
    _s_collection_name = 'Pet'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    species = Column(String)
    breed = Column(String)
    date_of_birth = Column(Date)
    customer_id = Column(ForeignKey('customer.id'))

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("PetList"))

    # child relationships (access children)
    AppointmentList : Mapped[List["Appointment"]] = relationship(back_populates="pet")
    PetServiceList : Mapped[List["PetService"]] = relationship(back_populates="pet")



class ProductSupply(SAFRSBaseX, Base):
    """
    description: Intermediate table to link products with suppliers.
    """
    __tablename__ = 'product_supply'
    _s_collection_name = 'ProductSupply'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    product_id = Column(ForeignKey('product.id'))
    supplier_id = Column(ForeignKey('supplier.id'))

    # parent relationships (access parent)
    product : Mapped["Product"] = relationship(back_populates=("ProductSupplyList"))
    supplier : Mapped["Supplier"] = relationship(back_populates=("ProductSupplyList"))

    # child relationships (access children)



class Shift(SAFRSBaseX, Base):
    """
    description: Table to store shift details for employees.
    """
    __tablename__ = 'shift'
    _s_collection_name = 'Shift'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    employee_id = Column(ForeignKey('employee.id'))
    start_time = Column(DateTime)
    end_time = Column(DateTime)

    # parent relationships (access parent)
    employee : Mapped["Employee"] = relationship(back_populates=("ShiftList"))

    # child relationships (access children)



class Appointment(SAFRSBaseX, Base):
    """
    description: Table to store appointment details for pet services.
    """
    __tablename__ = 'appointment'
    _s_collection_name = 'Appointment'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    pet_id = Column(ForeignKey('pet.id'))
    service_type = Column(String)
    date = Column(DateTime)

    # parent relationships (access parent)
    pet : Mapped["Pet"] = relationship(back_populates=("AppointmentList"))

    # child relationships (access children)



class OrderItem(SAFRSBaseX, Base):
    """
    description: Table to store details of order items.
    """
    __tablename__ = 'order_item'
    _s_collection_name = 'OrderItem'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    order_id = Column(ForeignKey('order.id'))
    product_id = Column(ForeignKey('product.id'))
    quantity = Column(Integer, nullable=False)
    item_total = Column(Integer)

    # parent relationships (access parent)
    order : Mapped["Order"] = relationship(back_populates=("OrderItemList"))
    product : Mapped["Product"] = relationship(back_populates=("OrderItemList"))

    # child relationships (access children)



class PetService(SAFRSBaseX, Base):
    """
    description: Intermediate table to link services provided to pets.
    """
    __tablename__ = 'pet_service'
    _s_collection_name = 'PetService'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    pet_id = Column(ForeignKey('pet.id'))
    service_id = Column(ForeignKey('service.id'))
    appointment_date = Column(DateTime)

    # parent relationships (access parent)
    pet : Mapped["Pet"] = relationship(back_populates=("PetServiceList"))
    service : Mapped["Service"] = relationship(back_populates=("PetServiceList"))

    # child relationships (access children)
