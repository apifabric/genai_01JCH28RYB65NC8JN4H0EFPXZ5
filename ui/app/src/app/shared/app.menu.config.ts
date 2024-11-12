import { MenuRootItem } from 'ontimize-web-ngx';

import { AppointmentCardComponent } from './Appointment-card/Appointment-card.component';

import { CustomerCardComponent } from './Customer-card/Customer-card.component';

import { EmployeeCardComponent } from './Employee-card/Employee-card.component';

import { OrderCardComponent } from './Order-card/Order-card.component';

import { OrderItemCardComponent } from './OrderItem-card/OrderItem-card.component';

import { PetCardComponent } from './Pet-card/Pet-card.component';

import { PetServiceCardComponent } from './PetService-card/PetService-card.component';

import { ProductCardComponent } from './Product-card/Product-card.component';

import { ProductSupplyCardComponent } from './ProductSupply-card/ProductSupply-card.component';

import { ServiceCardComponent } from './Service-card/Service-card.component';

import { ShiftCardComponent } from './Shift-card/Shift-card.component';

import { SupplierCardComponent } from './Supplier-card/Supplier-card.component';


export const MENU_CONFIG: MenuRootItem[] = [
    { id: 'home', name: 'HOME', icon: 'home', route: '/main/home' },
    
    {
    id: 'data', name: ' data', icon: 'remove_red_eye', opened: true,
    items: [
    
        { id: 'Appointment', name: 'APPOINTMENT', icon: 'view_list', route: '/main/Appointment' }
    
        ,{ id: 'Customer', name: 'CUSTOMER', icon: 'view_list', route: '/main/Customer' }
    
        ,{ id: 'Employee', name: 'EMPLOYEE', icon: 'view_list', route: '/main/Employee' }
    
        ,{ id: 'Order', name: 'ORDER', icon: 'view_list', route: '/main/Order' }
    
        ,{ id: 'OrderItem', name: 'ORDERITEM', icon: 'view_list', route: '/main/OrderItem' }
    
        ,{ id: 'Pet', name: 'PET', icon: 'view_list', route: '/main/Pet' }
    
        ,{ id: 'PetService', name: 'PETSERVICE', icon: 'view_list', route: '/main/PetService' }
    
        ,{ id: 'Product', name: 'PRODUCT', icon: 'view_list', route: '/main/Product' }
    
        ,{ id: 'ProductSupply', name: 'PRODUCTSUPPLY', icon: 'view_list', route: '/main/ProductSupply' }
    
        ,{ id: 'Service', name: 'SERVICE', icon: 'view_list', route: '/main/Service' }
    
        ,{ id: 'Shift', name: 'SHIFT', icon: 'view_list', route: '/main/Shift' }
    
        ,{ id: 'Supplier', name: 'SUPPLIER', icon: 'view_list', route: '/main/Supplier' }
    
    ] 
},
    
    { id: 'settings', name: 'Settings', icon: 'settings', route: '/main/settings'}
    ,{ id: 'about', name: 'About', icon: 'info', route: '/main/about'}
    ,{ id: 'logout', name: 'LOGOUT', route: '/login', icon: 'power_settings_new', confirm: 'yes' }
];

export const MENU_COMPONENTS = [

    AppointmentCardComponent

    ,CustomerCardComponent

    ,EmployeeCardComponent

    ,OrderCardComponent

    ,OrderItemCardComponent

    ,PetCardComponent

    ,PetServiceCardComponent

    ,ProductCardComponent

    ,ProductSupplyCardComponent

    ,ServiceCardComponent

    ,ShiftCardComponent

    ,SupplierCardComponent

];