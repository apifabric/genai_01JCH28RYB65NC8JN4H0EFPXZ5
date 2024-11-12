import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'PetService-new',
  templateUrl: './PetService-new.component.html',
  styleUrls: ['./PetService-new.component.scss']
})
export class PetServiceNewComponent {
  @ViewChild("PetServiceForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}