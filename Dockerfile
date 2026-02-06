# Dockerfile to build the validmind-docs image

# Use the official Nginx image
FROM nginx:alpine

# Install jq for better JSON handling
RUN apk add --no-cache jq

# Security Upgrade Zone
RUN apk upgrade --no-cache libxml2 libexpat

# Copy the static site content to the Nginx HTML directory
COPY site/_site /usr/share/nginx/html

# Copy validmind-docs.yaml for fallback URL values
COPY site/validmind-docs.yaml /usr/share/nginx/html/validmind-docs.yaml

# Copy the URL replacement script
COPY site/scripts/docker_entrypoint.sh /docker-entrypoint.d/40-replace-placeholders.sh

# Make the URL replacement script executable
RUN chmod +x /docker-entrypoint.d/40-replace-placeholders.sh

# Expose port 4444
EXPOSE 4444
