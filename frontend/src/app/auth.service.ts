import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse, HttpParams } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, tap } from 'rxjs/operators';
import { environment } from '../environments/environment';  // Importe o environment

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private loginUrl = environment.loginUrl;
  private logoutUrl = environment.loginUrl;

  constructor(private http: HttpClient) {}

login(email: string, password: string): Observable<any> {
  const body = `email=${encodeURIComponent(email)}&password=${encodeURIComponent(password)}`;

  return this.http.post(this.loginUrl, body, {
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    withCredentials: true,
  });
}

  async logout(): Promise<any> {
    return this.http.post(this.loginUrl + 'logout/', {}, {
      withCredentials: true
    });
  }
}