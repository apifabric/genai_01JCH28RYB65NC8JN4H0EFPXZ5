import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { MainComponent } from './main.component';

export const routes: Routes = [
  {
    path: '', component: MainComponent,
    children: [
        { path: '', redirectTo: 'home', pathMatch: 'full' },
        { path: 'about', loadChildren: () => import('./about/about.module').then(m => m.AboutModule) },
        { path: 'home', loadChildren: () => import('./home/home.module').then(m => m.HomeModule) },
        { path: 'settings', loadChildren: () => import('./settings/settings.module').then(m => m.SettingsModule) },
      
    
        { path: 'Appointment', loadChildren: () => import('./Appointment/Appointment.module').then(m => m.AppointmentModule) },
    
        { path: 'Customer', loadChildren: () => import('./Customer/Customer.module').then(m => m.CustomerModule) },
    
        { path: 'Employee', loadChildren: () => import('./Employee/Employee.module').then(m => m.EmployeeModule) },
    
        { path: 'Order', loadChildren: () => import('./Order/Order.module').then(m => m.OrderModule) },
    
        { path: 'OrderItem', loadChildren: () => import('./OrderItem/OrderItem.module').then(m => m.OrderItemModule) },
    
        { path: 'Pet', loadChildren: () => import('./Pet/Pet.module').then(m => m.PetModule) },
    
        { path: 'PetService', loadChildren: () => import('./PetService/PetService.module').then(m => m.PetServiceModule) },
    
        { path: 'Product', loadChildren: () => import('./Product/Product.module').then(m => m.ProductModule) },
    
        { path: 'ProductSupply', loadChildren: () => import('./ProductSupply/ProductSupply.module').then(m => m.ProductSupplyModule) },
    
        { path: 'Service', loadChildren: () => import('./Service/Service.module').then(m => m.ServiceModule) },
    
        { path: 'Shift', loadChildren: () => import('./Shift/Shift.module').then(m => m.ShiftModule) },
    
        { path: 'Supplier', loadChildren: () => import('./Supplier/Supplier.module').then(m => m.SupplierModule) },
    
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class MainRoutingModule { }