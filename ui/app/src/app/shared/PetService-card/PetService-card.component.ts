import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './PetService-card.component.html',
  styleUrls: ['./PetService-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.PetService-card]': 'true'
  }
})

export class PetServiceCardComponent {


}