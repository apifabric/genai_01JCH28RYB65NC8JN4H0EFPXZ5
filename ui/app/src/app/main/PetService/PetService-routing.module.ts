import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PetServiceHomeComponent } from './home/PetService-home.component';
import { PetServiceNewComponent } from './new/PetService-new.component';
import { PetServiceDetailComponent } from './detail/PetService-detail.component';

const routes: Routes = [
  {path: '', component: PetServiceHomeComponent},
  { path: 'new', component: PetServiceNewComponent },
  { path: ':id', component: PetServiceDetailComponent,
    data: {
      oPermission: {
        permissionId: 'PetService-detail-permissions'
      }
    }
  }
];

export const PETSERVICE_MODULE_DECLARATIONS = [
    PetServiceHomeComponent,
    PetServiceNewComponent,
    PetServiceDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class PetServiceRoutingModule { }