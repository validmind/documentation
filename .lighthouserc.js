module.exports = {
  ci: {
    collect: {
      staticDistDir: 'site/_site',
      startServerCommand: 'npx serve site/_site -p 8080',
      url: ['http://localhost:8080/index.html'],
    },
    assert: {
      assertions: {
        'categories:accessibility': ['error', { minScore: 0.9 }],
      },
    },
    upload: {
      target: 'temporary-public-storage',
    },
  },
}; 