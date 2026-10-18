from langchain_community.tools import DuckDuckGoSearchRun
search_tool = DuckDuckGoSearchRun();

result = search_tool.invoke('Top news in India')
print(result);

print("\n ----------- \n")