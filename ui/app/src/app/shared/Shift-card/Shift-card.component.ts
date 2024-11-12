import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Shift-card.component.html',
  styleUrls: ['./Shift-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Shift-card]': 'true'
  }
})

export class ShiftCardComponent {


}