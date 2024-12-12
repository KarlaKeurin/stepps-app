import { Component } from '@angular/core';
import { AuthService } from '../../auth.service';
import { FormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import { tap, catchError } from 'rxjs/operators';
import { of } from 'rxjs';

@Component({
  selector: 'app-login',
  // standalone: true,
  imports: [FormsModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})

export class LoginComponent {
  email: string = '';
  password: string = '';

  constructor(private authService: AuthService, private router: Router) { }

  onSubmit() {
    const loginData = { email: this.email, password: this.password };

    this.authService.login(loginData.email, loginData.password)
      .subscribe({
        next: response => {
          alert('Login successful');
          localStorage.setItem('user', JSON.stringify(response));
          this.router.navigate(['/dashboard']);
        },
        error: error => {
          console.error('Login error:', error);
          alert('Login failed');
    }
  })
}}
