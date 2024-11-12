import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {PETSERVICE_MODULE_DECLARATIONS, PetServiceRoutingModule} from  './PetService-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    PetServiceRoutingModule
  ],
  declarations: PETSERVICE_MODULE_DECLARATIONS,
  exports: PETSERVICE_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class PetServiceModule { }