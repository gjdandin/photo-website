# photo-portfolio-website

A photographer portfolio website made for a client. 
It has the following (mobile/tablet responsive) pages:
  
  Front-end:
  - Index homepage (Showcases the "best" photos that the client wants to show).
  - Photo album page 
    - showcases either all images, different albums and includes a search and filter feature connected to the backend that filters based on album, photo title and photographer.
  - About us page
  - Contact page (with a contact/message form that once sent, generates an email with a copy of the message and sender details and sends this directly to the clients email adress).
  - Login page for admins, includes an email-based password reset option.
  
  Backend-pages (invisible to non-admins):
  - Photo upload page 
    - Upload form that once submitted, creates and uploads an image object to the backend. 
    - A photograph object is then connected to a certain user(photographer) and an album. One-to-many relationship for Photographer and album to photos.
  - Photo edit page, the admin can change the details of a photograph, such as album, photographer, title etc.
    - Includes a delete option
  - Django backend for album&user object creation.
  
  Noteworthy feature:
  - All front-end pages(exception of homepage) have a light&dark mode toggle button.
    - this was a request made by client because the website could feel too "dark" combined with photographs that have a dark theme.
  
  Technologies used:
  - Python Django as both frontend(HTML templates) and backend(database) handler. Custom-made image, album and user models and page views.
  - Javascript and JQuery
  - boto3 and django-storages to connect to Amazon AWS CDN (bucket and cloudfront). The website is fully uploaded to Amazon cloud.
  - PILkit, pillow and easy-thumbnails to show images
  - django-compressor, django-compression-middleware, brotli and django-resized to compress large files and optimize page load.
  - Django-heroku. Hosted on heroku free version.
  
  Future features:
  - Some pages are incomplete(content wise) and lacks text.
  - Links to socials.
  
  Credits: 
  Some pages are based on the following templates, but are heavily modified:
  - https://templatemo.com/tm-520-highway
  - https://html5up.net/solid-state
  
  Special thanks to the YT channel Dennis Ivy for learning me how to create a django website:
  https://www.youtube.com/channel/UCTZRcDjjkVajGL6wd76UnGg
