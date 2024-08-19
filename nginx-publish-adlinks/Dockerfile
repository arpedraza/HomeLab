# Use the official Nginx image from the Docker Hub
FROM nginx:alpine

# Copy the text file and HTML file into the default Nginx public directory
COPY combined_hosts.txt /usr/share/nginx/html/
COPY index.html /usr/share/nginx/html/

# Expose port 80 to the host machine
EXPOSE 80