import { Component } from '@angular/core';
import { DashboardService } from './dashboard.service';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { AuthService } from '../../auth.service';

@Component({
  selector: 'app-dashboard',
  imports: [],
  templateUrl: './dashboard.component.html',
  styleUrl: './dashboard.component.css'
})
export class DashboardComponent {
  data: any;
  username: string | null = null;

  constructor(
    private dashboardService: DashboardService, 
    private router: Router,
    private authService: AuthService
  ) {}

  ngOnInit(): void {
    const userData = localStorage.getItem('user');
    if (userData) {
      const user = JSON.parse(userData);
      this.username = user.username;
    }
    // console.log(this.data);
    this.dashboardService.getDashboardData().subscribe((response) => {
      this.data = response;
      console.log(this.data);
    });
  }

  logout(): void { 
    this.authService.logout()
    .then(() => { 
      localStorage.removeItem('user'); 
      this.router.navigate(['/']); 
    }); 
  }
}
