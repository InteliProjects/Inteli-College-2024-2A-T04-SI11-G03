import { Component } from '@angular/core';
import { DividerModule } from 'primeng/divider';

@Component({
  selector: 'app-invoicing-table',
  standalone: true,
  imports: [DividerModule],
  templateUrl: './invoicing-table.component.html',
  styleUrl: './invoicing-table.component.css'
})
export class InvoicingTableComponent {

}
