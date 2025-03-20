class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        parent = list(range(n))  # 初始化每個節點的父節點為自己，形成獨立的集合
        
        min_path_cost = [-1] * n  # 儲存每個集合的最小路徑成本，初始值為-1（全1的二進位表示）
        
        def find_root(node: int) -> int:  # 尋找節點所在集合的根節點（帶路徑壓縮）
            if parent[node] != node:  # 如果節點不是自己的父節點
                parent[node] = find_root(parent[node])  # 遞迴尋找根節點並壓縮路徑
            return parent[node]  # 返回根節點
        
        # 處理每條邊，構建集合並計算最小成本
        for source, target, weight in edges:
            source_root = find_root(source)  # 找到起點的根節點
            target_root = find_root(target)  # 找到終點的根節點
            
            min_path_cost[target_root] &= weight  # 更新目標根節點的最小成本（位元AND運算）
            
            if source_root != target_root:  # 如果起點和終點不在同一個集合
                min_path_cost[target_root] &= min_path_cost[source_root]  # 合併集合時更新最小成本
                parent[source_root] = target_root  # 將起點的根節點指向目標根節點，合併集合
        
        result = []  # 儲存查詢結果的列表
        # 處理每個查詢
        for start, end in query:
            if start == end:  # 如果起點和終點相同
                result.append(0)  # 成本為0
            elif find_root(start) != find_root(end):  # 如果起點和終點不在同一個集合
                result.append(-1)  # 返回-1表示無法到達
            else:  # 如果起點和終點在同一個集合
                result.append(min_path_cost[find_root(start)])  # 返回該集合的最小成本
                
        return result  # 返回所有查詢的結果
