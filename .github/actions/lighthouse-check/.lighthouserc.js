module.exports = {
  ci: {
    collect: {
      staticDistDir: 'site/_site',
      url: [
        'http://localhost:8080/index.html',
        'http://localhost:8080/get-started/get-started.html',
        'http://localhost:8080/guide/guides.html',
        'http://localhost:8080/developer/validmind-library.html',
        'http://localhost:8080/support/support.html',
        'http://localhost:8080/releases/all-releases.html',
        'http://localhost:8080/training/training.html',
        // Add more URLs as needed
      ],
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