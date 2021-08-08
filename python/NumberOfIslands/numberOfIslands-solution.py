class Solution:
    def merge(self, label1, label2):
        labels = self.label_island_map[label1]
        for i in labels:
            self.island_label[i] = label2
            self.label_island_map[label2].append(i)
        del self.label_island_map[label1]
        
        
    def check_merge(self, label1, label2):
        label1_len = len(self.label_island_map[label1])
        label2_len = len(self.label_island_map[label2])
        if(label1_len<=label2_len):
            self.merge(label1,label2)
            return label2
        else:
            self.merge(label2,label1)
            return label1
            
    def numIslands(self, grid: List[List[str]]) -> int:
        self.island_label = {}
        self.label_island_map = {}
        self.max_label_count = 0 
        m = len(grid)
        n = len(grid[0])
        for row in range(m):
            for col in range(n):
                label = None
                if grid[row][col]!='1':
                    continue
                if((row-1)>=0  and grid[row-1][col]=='1'):
                    label = self.island_label[(row-1,col)]
                if((col-1)>=0  and grid[row][col-1]=='1'):
                    if label is None:
                        label = self.island_label[(row,col-1)]
                    elif((self.island_label.get((row,col-1),None) is not None) and
                         (label != self.island_label.get((row,col-1),None))):
                        label = self.check_merge(label,self.island_label[(row,col-1)])
                if(label is None):
                    self.max_label_count+=1
                    label = self.max_label_count
                self.island_label[(row,col)] = label
                self.label_island_map[label] = self.label_island_map.get(label,[])
                self.label_island_map[label].append((row,col))
        return len(self.label_island_map)
                
                        
