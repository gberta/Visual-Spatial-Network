function [seg_mask]=mcg_projection(coarse_mask,mcg_candidates)
    
    
    height=size(coarse_mask,1);
    width=size(coarse_mask,2);
    
    seg_mask=zeros(height,width); 
    
    scores=mcg_candidates.scores;
    
    [V,I]=sort(scores,'descend');
    
    K=min(size(I,1),750);
    
    sp=mcg_candidates.superpixels; %superpixels
    
    fprintf('Labeling Regions...\n');
    for j=1:K
       i=I(j);
       
       region = ismember(sp, mcg_candidates.labels{i}); 
       region_ind=find(region==1);
       region_mean_gt=mean(coarse_mask(region_ind));
       
       seg_mask(region_ind)=max(seg_mask(region_ind),region_mean_gt);

            
    end

    
    fprintf('Done\n');
end