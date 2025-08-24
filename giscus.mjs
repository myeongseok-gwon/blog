/**
 * MyST JavaScript Plugin for Giscus Comments
 * Adds Giscus comments system to all pages
 */

const giscusTransform = {
  name: 'giscus-comments',
  doc: 'Adds Giscus comments system to all pages',
  stage: 'document',
  plugin: (_, utils) => (node) => {
    // Add Giscus script to the end of each document
    const giscusScript = {
      type: 'html',
      value: `
        <div class="giscus" style="margin-top: 2rem; padding-top: 2rem; border-top: 1px solid #e1e4e8;">
          <script src="https://giscus.app/client.js"
                  data-repo="myeongseok-gwon/blog"
                  data-repo-id="R_kgDONNXfQw"
                  data-category="Announcements"
                  data-category-id="DIC_kwDONNXfQ84Cuhyx"
                  data-mapping="pathname"
                  data-strict="0"
                  data-reactions-enabled="1"
                  data-emit-metadata="0"
                  data-input-position="bottom"
                  data-theme="preferred_color_scheme"
                  data-lang="ko"
                  crossorigin="anonymous"
                  async>
          </script>
        </div>
      `
    };
    
    // Add the script to the end of the document
    if (node.children) {
      node.children.push(giscusScript);
    }
  },
};

const plugin = {
  name: 'Giscus Comments',
  author: 'Myeongseok Gwon',
  license: 'MIT',
  transforms: [giscusTransform],
};

export default plugin;
