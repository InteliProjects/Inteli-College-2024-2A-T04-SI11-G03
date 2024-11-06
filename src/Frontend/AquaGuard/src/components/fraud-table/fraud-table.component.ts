import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TableModule } from 'primeng/table';
import { PaginatorModule } from 'primeng/paginator';
import { FormsModule } from '@angular/forms';
import { MatSelectModule } from '@angular/material/select';
import { MatDialog, MatDialogModule } from '@angular/material/dialog'; 
import { CustomerDetailsModalComponent } from '../customer-details-modal/customer-details-modal.component';

@Component({
  selector: 'app-fraud-table',
  standalone: true,
  imports: [MatSelectModule, FormsModule, PaginatorModule, TableModule, CommonModule, MatDialogModule],
  templateUrl: './fraud-table.component.html',
  styleUrl: './fraud-table.component.css'
})
export class FraudTableComponent {
  customers: any[] = [];
  rowsPerPage = 10;
  rowsPerPageOptions: number[] = [];
  statusOptions = [
    { label: 'Em aberto', color: '#EC6E13' },
    { label: 'Em análise', color: '#1B7AC3' },
    { label: 'Em Fiscalização', color: '#FFD600' },
    { label: 'Fiscalizado S/ Fraude', color: '#6BB70B' },
    { label: 'Fiscalizado C/ Fraude', color: '#8D2323' },
    { label: 'Não Fraude', color: '#608724' },
    { label: 'Fraude', color: '#C64B52' },
    { label: 'Sem status', color: '#A9A9A9' },
  ];

  constructor(public dialog: MatDialog) {
    for (let i = 1; i <= 100; i++) {
      const matricula = this.generateMatricula();
      this.customers.push({
        id: matricula,
        maskedId: this.maskMatricula(matricula),
        averageConsumption: this.getRandomConsumption(),
        balance: this.getRandomBalance(),
        latitude: this.getRandomCoordinate(),
        longitude: this.getRandomCoordinate(),
        fraudPercentage: this.getRandomFraudPercentage(),
        status: this.statusOptions[7].label, 
      });
    }

    this.generateRowsPerPageOptions();
  }

  onActionClick(customer: any): void {
    this.dialog.open(CustomerDetailsModalComponent, {
      data: customer,
      width: '400px',
    });
  }

  generateMatricula() {
    return Math.floor(1000000 + Math.random() * 9000000).toString();
  }

  maskMatricula(matricula: string) {
    return `${matricula.substring(0, 2)}XXX${matricula.substring(5, 7)}`;
  }

  generateRowsPerPageOptions() {
    const totalCustomers = this.customers.length;
    this.rowsPerPageOptions = [];
    for (let i = 5; i <= totalCustomers && i <= 50; i += 5) {
      this.rowsPerPageOptions.push(i);
    }
  }

  getRandomConsumption() {
    return Math.floor(Math.random() * 100) + 1;
  }

  getRandomBalance() {
    return Math.floor(Math.random() * 5000) + 100;
  }

  getRandomCoordinate() {
    return (Math.random() * (90 - -90) + -90).toFixed(6);
  }

  getRandomFraudPercentage() {
    return Math.floor(Math.random() * 100);
  }

  getStatusColor(status: string): string {
    const option = this.statusOptions.find((opt) => opt.label === status);
    return option ? option.color : 'black'; 
  }
}
