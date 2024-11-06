import { Component } from '@angular/core';
import { MatInputModule } from '@angular/material/input';
import { MatIconModule } from '@angular/material/icon';
import { MatFormFieldModule } from '@angular/material/form-field';
import { FormsModule } from '@angular/forms';  

@Component({
  selector: 'app-search',
  standalone: true,
  imports: [    
    MatInputModule,
    MatIconModule,
    MatFormFieldModule,
    FormsModule  
  ],
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css']
})
export class SearchComponent {
  searchTerm: string = '';
}
