import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'Shift-new',
  templateUrl: './Shift-new.component.html',
  styleUrls: ['./Shift-new.component.scss']
})
export class ShiftNewComponent {
  @ViewChild("ShiftForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}