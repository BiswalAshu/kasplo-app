# Use the official Nginx image as a base image
FROM nginx:alpine

# Copy the HTML file into the default Nginx public directory
COPY index.html /usr/share/nginx/html/index.html


# Expose port 80 to the outside world
EXPOSE 80

# Command to start Nginx
CMD ["nginx", "-g", "daemon off;"]

