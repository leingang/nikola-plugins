from nikola.plugin_categories import ConfigPlugin

class CategoryMenu(ConfigPlugin):
    """Add category menu to global context"""

    name = "category_menu"

    def set_site(self,site):
        site.scan_posts()
        # count posts in each category
        cat_count={}
        for cat,posts in site.posts_per_category.items():
            cat_count[cat] = len(posts)
        # this list of tuples has fields like so:
        # * "base name" of category
        # * "full name" of category (as a '/'-joined path)
        # * "path list" of category (list of branches)
        # * link to category index page
        # * count of posts in this category
        cat_hierarchy = [(node.name, node.category_name, node.category_path,
                            site.link("category", node.category_name),
                            cat_count[node.category_name])
                        for node in site.category_hierarchy]
        # dict for consolidating post count by top level category
        tlcats={}
        for lang in site.config['NAVIGATION_LINKS'].values:
            for basename,fullname,pathlist,link,count in cat_hierarchy:
                tlname=pathlist[0]
                if (basename==tlname):
                    # top level
                    tlcats[tlname] = {'basename':basename,'link':link,'count':count}
                else:
                    tlfoo,tllink,tlcount = tlcats[tlname]
                    tlcats[tlname]['count'] += count
        # decorated list for sorting
        # we're going to pass the post count as a query string parameter,
        # so as not to not to break the base templates
        # (if the template doesn't know how to handle the post count, it will
        # get appended to the link harmlessly)
        tlcatlist=[
            (e['link'],e['count'],e['basename']) for e in tlcats.values()
        ]
        tlcatlist.sort(key=lambda e: int(e[1]),reverse=True)
        print(tlcatlist)
        site.GLOBAL_CONTEXT['CATEGORY_MENU'] = tlcatlist
        super(CategoryMenu,self).set_site(site)
