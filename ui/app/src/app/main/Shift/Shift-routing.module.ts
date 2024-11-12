import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ShiftHomeComponent } from './home/Shift-home.component';
import { ShiftNewComponent } from './new/Shift-new.component';
import { ShiftDetailComponent } from './detail/Shift-detail.component';

const routes: Routes = [
  {path: '', component: ShiftHomeComponent},
  { path: 'new', component: ShiftNewComponent },
  { path: ':id', component: ShiftDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Shift-detail-permissions'
      }
    }
  }
];

export const SHIFT_MODULE_DECLARATIONS = [
    ShiftHomeComponent,
    ShiftNewComponent,
    ShiftDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ShiftRoutingModule { }