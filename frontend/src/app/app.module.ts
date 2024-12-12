import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';
import { provideHttpClient, withInterceptorsFromDi } from '@angular/common/http'; // Importa o novo método
import { routes } from './app.routes';
import { RouterModule } from '@angular/router';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    RouterModule.forRoot(routes)
  ],
  providers: [
    provideHttpClient(withInterceptorsFromDi())  // Substitui o HttpClientModule pela nova configuração
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
