FROM node:18-alpine

# Set working directory
WORKDIR /app

# Copy package files first
COPY package*.json ./

# Install production dependencies only
RUN npm install --only=production

# Copy application file
COPY app.js .

# Set default environment variables
ENV NODE_ENV=production
ENV PORT=3000
ENV APP_VERSION=1.0.0

# Expose container port
EXPOSE 3000

# Start application
CMD ["node", "app.js"]