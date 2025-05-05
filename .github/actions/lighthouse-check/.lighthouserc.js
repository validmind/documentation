const fs = require('fs');
module.exports = {
  ci: {
    collect: {
      staticDistDir: 'site/_site',
      url: fs.readFileSync('lhci-urls.txt', 'utf-8').split('\n').filter(Boolean),
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