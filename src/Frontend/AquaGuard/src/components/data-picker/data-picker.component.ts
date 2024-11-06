import { Component } from '@angular/core';
import { CalendarModule } from 'primeng/calendar';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-data-picker',
  standalone: true,
  imports: [CalendarModule, FormsModule], 
  templateUrl: './data-picker.component.html',
  styleUrls: ['./data-picker.component.css']
})
export class DatapickerComponent {
  selectedDate: Date | null = null;
}
