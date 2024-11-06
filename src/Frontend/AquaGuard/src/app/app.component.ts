import { Component, EventEmitter, Output } from '@angular/core';
import { UploadComponent } from '../components/upload/upload.component';
import { RouterOutlet } from '@angular/router';
import { MonthlyConsumptionGraphComponent } from '../components/monthly-consumption-graph/monthly-consumption-graph.component';
import { ConsumptioTableComponent } from '../components/consumptio-table/consumptio-table.component';
import { InvoicingTableComponent } from '../components/invoicing-table/invoicing-table.component';
import { SearchComponent } from '../components/search/search.component';
import { FraudTableComponent } from '../components/fraud-table/fraud-table.component';
import { BothComponent } from '../components/both/both.component';
import { FormsModule } from '@angular/forms';
import { DatapickerComponent } from '../components/data-picker/data-picker.component';
import { Router } from '@angular/router';


@Component({
  selector: 'app-root',
  standalone: true,
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  imports: [RouterOutlet, UploadComponent, MonthlyConsumptionGraphComponent, ConsumptioTableComponent, InvoicingTableComponent, SearchComponent, FraudTableComponent, BothComponent, FormsModule, DatapickerComponent] 
})
export class AppComponent {
  title = 'angular-app';
  constructor(
    private router: Router,
  ){}

  defaultFontSizes: Map<HTMLElement, string> = new Map();

  decreaseLetter(){
    const elements = document.querySelectorAll('[class]');
    elements.forEach(element => {
      const computedStyle = window.getComputedStyle(element as HTMLElement);
      const fontSize = computedStyle.getPropertyValue('font-size');
      if (fontSize && fontSize !== 'initial') {
        const currentSize = parseFloat(fontSize);
        if (!isNaN(currentSize)) {
          const newSize = currentSize - 0.5;
          (element as HTMLElement).style.fontSize = `${newSize}px`;
          if (!this.defaultFontSizes.has(element as HTMLElement)) {
            this.defaultFontSizes.set(element as HTMLElement, fontSize);
          }
        }
      }
    });
  }

  normalLetter(){
    this.defaultFontSizes.forEach((fontSize, element) => {
      element.style.fontSize = fontSize;
    });
  }

  increaseLetter() {
    const elements = document.querySelectorAll('[class]');
    elements.forEach(element => {
      const computedStyle = window.getComputedStyle(element as HTMLElement);
      const fontSize = computedStyle.getPropertyValue('font-size');
      if (fontSize && fontSize !== 'initial') {
        const currentSize = parseFloat(fontSize);
        if (!isNaN(currentSize)) {
          const newSize = currentSize + 0.5;
          (element as HTMLElement).style.fontSize = `${newSize}px`;
          if (!this.defaultFontSizes.has(element as HTMLElement)) {
            this.defaultFontSizes.set(element as HTMLElement, fontSize);
          }
        }
      }
    });
  }

}
