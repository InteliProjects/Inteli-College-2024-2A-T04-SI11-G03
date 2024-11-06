import { Component } from '@angular/core';
import { TabMenuModule } from 'primeng/tabmenu';
import { RippleModule } from 'primeng/ripple';

@Component({
  selector: 'app-both',
  standalone: true,
  imports: [TabMenuModule, RippleModule],
  templateUrl: './both.component.html',
  styleUrls: ['./both.component.css']
})
export class BothComponent {
  items = [
    { label: 'Em aberto', image: 'assets/active.svg', id: 'open' },
    { label: 'Concluído', image: 'assets/disable.svg', id: 'completed' }
  ];

  activeItem = this.items[0]; 
  
  setActiveItem(event: any) {
    this.activeItem = event.item;
  }
}
