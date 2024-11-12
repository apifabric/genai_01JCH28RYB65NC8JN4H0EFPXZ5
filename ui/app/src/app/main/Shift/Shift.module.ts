import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {SHIFT_MODULE_DECLARATIONS, ShiftRoutingModule} from  './Shift-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    ShiftRoutingModule
  ],
  declarations: SHIFT_MODULE_DECLARATIONS,
  exports: SHIFT_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class ShiftModule { }