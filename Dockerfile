# Dockerfile to build the validmind-docs image

# Use the official Nginx image
FROM nginx:alpine

# Copy the static site content to the Nginx HTML directory
COPY site/_site /usr/share/nginx/html

# Expose port 4444
EXPOSE 4444

# Nginx starts automatically as the default CMD
