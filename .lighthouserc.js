module.exports = {
  ci: {
    collect: {
      staticDistDir: 'site/_site',
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